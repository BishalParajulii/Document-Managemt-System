import { useParams } from "react-router-dom";

const DocumentEditor = () => {
  const { id } = useParams();

  return (
    <div>
      <h2>Document Editor</h2>
      <p>Document ID: {id}</p>
    </div>
  );
};

export default DocumentEditor;
