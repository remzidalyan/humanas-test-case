<?php

namespace App\Http\Controllers\User;

use App\Http\Controllers\Controller;
use Carbon\Carbon;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\Http;

class ActivityCTRL extends Controller
{
    public function index(): JsonResponse
    {
        try {
            $response = Http::timeout(30)->get('https://case-test-api.humanas.io');

            if ($response->failed()) {
                return response()->json(['error' => 'Failed to fetch data'], $response->status());
            }

            $data = json_decode($response->body());
            collect($data->data->rows)->each(function ($user) {
                $this->averageRange($user);
                $this->linearRegression($user);
            });
            return response()->json($data);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Failed to fetch data', 'exception' => $e], 500);
        }
    }

    /**
     * Bu fonksiyon kullanıcının giriş tarihlerini alır ve ortalama aralığı hesaplar.
     * Tahmini bir sonraki giriş tarihini belirler.
     *
     * @param $user
     * @return void
     */
    private function averageRange($user): void
    {
        $logins = collect($user->logins)->map(fn($date) => Carbon::parse($date))->sort();
        $dayDiffs = $logins
            ->skip(1)
            ->values()
            ->map(function ($login, $index) use ($logins) {
                return $login->diffInDays($logins[$index]);
            });

        $averageDiff = round($dayDiffs->avg(), 2);
        $lastLogin = $logins->last();
        $predictedNextLogin = $lastLogin->copy()->addDays(round($averageDiff));

        $user->average_range = [
            'last_login' => $lastLogin,
            'average_interval_days' => $averageDiff,
            'predicted_next_login' => $predictedNextLogin,
        ];
    }

    /**
     * Bu fonksiyon kullanıcının giriş tarihlerini alır.
     * Doğrusal regresyon tahmini yapan servise giriş bilgilerini yollar.
     * Elde ettiği bilgiyi servis eder.
     *
     * @param $user
     * @return void
     */

    private function linearRegression($user): void
    {
        $logins = collect($user->logins)->map(fn($date) => Carbon::parse($date))->sort();
        $LRResponse = Http::post(config('app.ml_api_url') . '/api/linear-regression/predict', [
            'logins' => $logins->map(fn($date) => $date->format('Y-m-d\TH:i:s.u\Z'))->toArray(),
        ]);

        $user->linear_regression = json_decode($LRResponse->body());
    }
}
