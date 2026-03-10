import axios from "axios";
import { useState } from "react";

function ResearchForm({setReport}) {

  const [topic,setTopic] = useState("");

  const submitResearch = async () => {

    const res = await axios.post("http://127.0.0.1:8000/research",{
      topic:topic
    });

    setReport(res.data.report);
  }

  return (
    <div>

      <input
        placeholder="Enter research topic"
        onChange={(e)=>setTopic(e.target.value)}
      />

      <button onClick={submitResearch}>
        Generate Research
      </button>

    </div>
  );
}

export default ResearchForm;