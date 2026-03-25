import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import Login from "./pages/auth/Login";
import { AdminDashboard } from "./pages/dashboard/AdminDashboard";
import Employees from "./components/Employees";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";

const App = () => {
  return (
    <div>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute adminOnly={true}>
                <AdminDashboard />
              </ProtectedRoute>
            }
          >
            {/* Default dashboard view can be added later, redirecting to employees for now if needed, or just leave it */}
            <Route path="employees" element={<Employees />} />
          </Route>

          <Route
            path="*"
            element={<Navigate to="/login" />}
          />
        </Routes>
      </AuthProvider>
    </div>
  );
};

export default App;
