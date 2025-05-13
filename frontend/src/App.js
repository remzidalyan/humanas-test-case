import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import LoginComparisonTable from './LoginComparison/Table'; // Bileşeni doğru yoldan import ettiğinizden emin olun

import './App.css';

import moment from 'moment';
import 'moment/locale/tr';  // Türkçe dil desteğini import et

// Türkçe dil desteğini aktif et
moment.locale('tr');

function App() {
    return (
        <Router>
            <Routes>
                {/* Ana sayfa rotası */}
                <Route path="/" element={<LoginComparisonTable/>}/>
            </Routes>
        </Router>
    );
}

export default App;
