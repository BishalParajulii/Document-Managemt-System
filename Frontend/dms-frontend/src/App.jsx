import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Documents from "./pages/Documents";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/documents" element={<Documents />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
