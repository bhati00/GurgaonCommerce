import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import Registration from './components/Registration';
Router

const  App: React.FC = () => {

  return (
    <>  
    <Router>
    <Routes>
        <Route path="/" element={<Registration />} />
      </Routes>
    </Router>
    </>
  )
}

export default App
