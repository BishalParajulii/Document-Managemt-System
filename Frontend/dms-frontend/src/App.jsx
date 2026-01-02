import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Documents from "./pages/Documents";
import MyDocuments from "./pages/MyDocuments";
import ProtectedRoute from "./routes/ProtectedRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public */}
        <Route path="/" element={<Login />} />

        {/* Protected */}
        <Route
          path="/documents"
          element={
            <ProtectedRoute>
              <Documents />
            </ProtectedRoute>
          }
        />

        <Route
          path="/my-docs"
          element={
            <ProtectedRoute>
              <MyDocuments />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
