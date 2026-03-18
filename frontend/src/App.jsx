import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import Login from "./pages/auth/Login";
import { AdminDashboard } from "./pages/dashboard/AdminDashboard";
import ProtectedRoute from "./components/ProtectedRoute";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute adminOnly={true}>
              <AdminDashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="*"
          element={<Navigate to="/login" />}
        />
      </Routes>
    </div>
  );
};

export default App;
