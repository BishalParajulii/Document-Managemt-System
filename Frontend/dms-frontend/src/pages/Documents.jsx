import { useEffect, useState } from "react";
import api from "../api/axios";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import DocumentCard from "../components/DocumentCard";
import DocumentPreviewModal from "../components/DocumentPreviewModal";
import UploadModal from "../components/UploadModal";
import "../css/Documents.css";

const Documents = () => {
  const [docs, setDocs] = useState([]);
  const [active, setActive] = useState("all");
  const [previewFile, setPreviewFile] = useState(null);
  const [showUpload, setShowUpload] = useState(false);

  useEffect(() => {
    loadDocs();
  }, [active]);

  const loadDocs = async () => {
    try {
      const endpoint = active === "mine" ? "my-docs/" : "docs/";
      const res = await api.get(endpoint);
      setDocs(res.data);
    } catch (err) {
      console.error("Failed to load documents", err);
    }
  };

  const openPreview = (file) => {
    const url = file.startsWith("http")
      ? file
      : `http://127.0.0.1:8000${file}`;

    setPreviewFile(url);
  };

  return (
    <div className="documents-layout">
      <Sidebar active={active} setActive={setActive} />

      <div className="documents-main">
        {/* ✅ PASS onUpload */}
        <Topbar onUpload={() => setShowUpload(true)} />

        <div className="documents-grid">
          {docs.length > 0 ? (
            docs.map((doc) => (
              <DocumentCard
                key={doc.id}
                doc={doc}
                onOpen={openPreview}
              />
            ))
          ) : (
            <p className="empty-text">No documents found</p>
          )}
        </div>
      </div>

      {/* PREVIEW MODAL */}
      {previewFile && (
        <DocumentPreviewModal
          fileUrl={previewFile}
          onClose={() => setPreviewFile(null)}
        />
      )}

      {/* ✅ UPLOAD MODAL */}
      {showUpload && (
        <UploadModal
          onClose={() => setShowUpload(false)}
          onSuccess={loadDocs}
        />
      )}
    </div>
  );
};

export default Documents;
