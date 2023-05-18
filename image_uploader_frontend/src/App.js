// import logo from './logo.svg';
// import './App.css';
import Main from './components/Main';
import Header from './components/Header';
import Footer from './components/Footer';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

function App() {
  return (
    <>
      <Header />
      <Main />
      <Footer />
    </>
  );
}


export default App;
