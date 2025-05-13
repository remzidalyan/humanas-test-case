import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    CircularProgress,
    Typography
} from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import moment from "moment";

const LoginComparisonTable = () => {
    const [loginData, setLoginData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const apiUrl = process.env.REACT_APP_API_URL;

        // API'den veriyi çekme
        axios.get(`${apiUrl}/user/activities`)
            .then((response) => {
                setLoginData(response.data.data.rows);
                setLoading(false);
            })
            .catch((error) => {
                console.error('Veri alınırken hata oluştu:', error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh'}}>
                <CircularProgress/>
                <Typography variant="h6" style={{marginLeft: 20}}>Yükleniyor...</Typography>
            </div>
        );
    }

    return (
        <React.Fragment>
            <CssBaseline/>
            <Container>
                <TableContainer component={Paper}>
                    <Table sx={{maxHeight: 650}} stickyHeader aria-label="sticky table">
                        <TableHead>
                            <TableRow>
                                <TableCell></TableCell>
                                <TableCell></TableCell>
                                <TableCell colSpan={2}>Ortalama Gün Aralığı</TableCell>
                                <TableCell>Doğrusal Regresyon</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell>Kullanıcı Adı</TableCell>
                                <TableCell>Son Giriş Zamanı</TableCell>
                                <TableCell>Ortalama Gün Aralığı Değeri</TableCell>
                                <TableCell>Tahmini Giriş Tarihi</TableCell>
                                <TableCell>Tahmini Giriş Tarihi</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {loginData.map((user) => (
                                <TableRow key={user.id}>
                                    <TableCell>{user.name}</TableCell>
                                    <TableCell>{moment(user.average_range.last_login).format('LLL')}</TableCell>
                                    <TableCell>{user.average_range.average_interval_days}</TableCell>
                                    <TableCell>{moment(user.average_range.predicted_next_login).format('LLL')}</TableCell>
                                    <TableCell>{moment(user.linear_regression.predicted_next_login).format('LLL')}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Container>
        </React.Fragment>
    );
};

export default LoginComparisonTable;
