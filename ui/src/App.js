import React from 'react';
import {
  Routes,
  Route,
  BrowserRouter,
} from "react-router-dom";
import './App.css';
import Index from './pages/Index';
import SignUp from './pages/SignUp';
import UserPage from './pages/UserPage'

function App() {
  return (
    <div className='App'>
≈    <BrowserRouter>
      <Routes>
          <Route path="sign-up" element={<SignUp />} />
          <Route path="sign-up/employee" element={<SignUp role={"employee"} />} />
          <Route path="userpage" element={<UserPage />} />
          <Route path="*" element={<Index />} /><Route path="/" element={<Index />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
