import { Navigate } from "react-router-dom";

const ProtectedRoute = ({
  children,
  adminOnly = false,
}) => {
  const user = JSON.parse(localStorage.getItem("user"));
  const token = localStorage.getItem("access_token");

  if (!token || !user) {
    return <Navigate to="/login" replace />;
  }

  if (adminOnly && !user.is_superuser) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default ProtectedRoute;
