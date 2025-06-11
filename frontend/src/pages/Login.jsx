import { useEffect } from "react";
import axios from "axios";

const Login = () => {
  useEffect(() => {
    /* global google */
    google.accounts.id.initialize({
      client_id: "414836687293-duqfoajjn7pi0a4qbv1gi50khoufcuun.apps.googleusercontent.com",
      callback: handleCredentialResponse,
    });

    google.accounts.id.renderButton(
      document.getElementById("g-signin"),
      { theme: "outline", size: "large" }
    );

    // Optionally prompt One Tap
    // google.accounts.id.prompt();
  }, []);

  async function handleCredentialResponse(response) {
    try {
      // Send Google ID token to backend to verify and get your app JWT
      const res = await axios.post("http://localhost:8000/auth/callback", {
        credential: response.credential,
      });

      const token = res.data.token;  // Your JWT from backend
      localStorage.setItem("token", token);  // Save token under key "token"
      window.location.href = "/chat";  // Redirect to chat page
    } catch (error) {
      console.error("Login failed:", error);
      alert("Login failed. Check console for details.");
    }
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Login with Google</h2>
      <div id="g-signin"></div>
    </div>
  );
};

export default Login;
