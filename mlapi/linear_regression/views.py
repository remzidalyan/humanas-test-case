<<<<<<< HEAD
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta, timezone
import numpy as np


class PredictNextLoginLinearRegressionView(APIView):
    @staticmethod
    # Bu metod, kullanıcının giriş tarihlerini alır.
    # Bir sonraki giriş tarihini lineer regresyon modeli ile tahmin eder.

    def post(request):
        login_dates = request.data.get('logins', [])

        if len(login_dates) < 2:
            return Response({'error': 'En az 2 giriş tarihi gereklidir.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_objects = [datetime.fromisoformat(d.replace('Z', '+00:00')) for d in login_dates]
            base_date = date_objects[0]

            # X: giriş yapılan gün sayıları (t1, t2, ...)
            # y: bir sonraki giriş günleri (t2, t3, ...)
            X = np.array([(d - base_date).days for d in date_objects[:-1]]).reshape(-1, 1)
            y = np.array([(d - base_date).days for d in date_objects[1:]])
            # X ve y dizilerini oluşturur.
            # X dizisi, giriş yapılan gün sayılarından oluşur.
            # y dizisi ise bir sonraki giriş günlerini içerir.

            # Linear Regression modelini oluşturur ve eğitir.
            model = LinearRegression()
            model.fit(X, y)

            # Son giriş tarihini kullanarak bir sonraki giriş tarihini tahmin eder.
            last_day = (date_objects[-1] - base_date).days
            predicted_day = model.predict(np.array([[last_day]])).item()

            predicted_date = base_date + timedelta(days=round(predicted_day))

            # Değerleri istenilen formata çevirerek servis eder.
            return Response({
                'last_login': date_objects[-1].astimezone(timezone.utc).isoformat().replace('+00:00', 'Z'),
                'predicted_next_login': predicted_date.astimezone(timezone.utc).isoformat(
                    timespec='microseconds').replace('+00:00', 'Z')
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta, timezone
import numpy as np


class PredictNextLoginLinearRegressionView(APIView):
    @staticmethod
    # Bu metod, kullanıcının giriş tarihlerini alır.
    # Bir sonraki giriş tarihini lineer regresyon modeli ile tahmin eder.

    def post(request):
        login_dates = request.data.get('logins', [])

        if len(login_dates) < 2:
            return Response({'error': 'En az 2 giriş tarihi gereklidir.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_objects = [datetime.fromisoformat(d.replace('Z', '+00:00')) for d in login_dates]
            base_date = date_objects[0]

            # X: giriş yapılan gün sayıları (t1, t2, ...)
            # y: bir sonraki giriş günleri (t2, t3, ...)
            X = np.array([(d - base_date).days for d in date_objects[:-1]]).reshape(-1, 1)
            y = np.array([(d - base_date).days for d in date_objects[1:]])
            # X ve y dizilerini oluşturur.
            # X dizisi, giriş yapılan gün sayılarından oluşur.
            # y dizisi ise bir sonraki giriş günlerini içerir.

            # Linear Regression modelini oluşturur ve eğitir.
            model = LinearRegression()
            model.fit(X, y)

            # Son giriş tarihini kullanarak bir sonraki giriş tarihini tahmin eder.
            last_day = (date_objects[-1] - base_date).days
            predicted_day = model.predict(np.array([[last_day]])).item()

            predicted_date = base_date + timedelta(days=round(predicted_day))

            # Değerleri istenilen formata çevirerek servis eder.
            return Response({
                'last_login': date_objects[-1].astimezone(timezone.utc).isoformat().replace('+00:00', 'Z'),
                'predicted_next_login': predicted_date.astimezone(timezone.utc).isoformat(
                    timespec='microseconds').replace('+00:00', 'Z')
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
>>>>>>> 6c728f5 (Conflict Resolve)
