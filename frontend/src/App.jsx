import React from "react";
import { Route, Routes } from "react-router-dom";
import Login from "./pages/auth/Login";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/login" element={<Login />} />
      </Routes>
    </div>
  );
};

export default App;
