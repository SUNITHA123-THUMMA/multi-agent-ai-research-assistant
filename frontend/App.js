import ResearchForm from "./components/ResearchForm";
import ReportViewer from "./components/ReportViewer";
import { useState } from "react";

function App() {

  const [report,setReport] = useState("");

  return (
    <div>
      <h1>AI Research Assistant</h1>
      <ResearchForm setReport={setReport}/>
      <ReportViewer report={report}/>
    </div>
  );
}

export default App;