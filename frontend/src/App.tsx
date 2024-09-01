import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import Registration from './components/Registration';
import UserProfile from './components/UserProfile';
Router

const  App: React.FC = () => {

  return (
    <>  
    <Router>
    <Routes>
        <Route path="/" element={<Registration />} />
        <Route path='user-profile' element={<UserProfile/>}></Route>
      </Routes>
    </Router>
    </>
  )
}

export default App
