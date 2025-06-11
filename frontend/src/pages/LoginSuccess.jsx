import React, { useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { setToken, isAuthenticated } from "../utils/auth";

const LoginSuccess = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const token = params.get("token");
    if (token) {
      setToken(token);
      navigate("/chat");
    } else if (isAuthenticated()) {
      navigate("/chat");
    }
  }, [location, navigate]);

  return <div>Redirecting...</div>;
};

export default LoginSuccess;
