import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Chat from "./chat";
import Login from "./login"; // Your Google Login page

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/chat" element={<Chat />} />
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
