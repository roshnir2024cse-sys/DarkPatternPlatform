import { useEffect, useState } from "react";
import API from "../services/api";

const History = () => {

  const [history, setHistory] = useState([]);

  useEffect(() => {

    fetchHistory();

  }, []);

  const fetchHistory = async () => {

    try {

      const res = await API.get("/history");

      setHistory(res.data);

    } catch (err) {

      console.log(err);

    }

  };

  return (

    <section className="max-w-6xl mx-auto py-20">

      <h2 className="text-4xl font-bold mb-8">

        📜 Prediction History

      </h2>

      <div className="space-y-5">

        {history.map((item) => (

          <div
            key={item.id}
            className="bg-white/5 border border-cyan-500/20 rounded-2xl p-6"
          >

            <div className="flex justify-between">

              <h3 className="text-xl font-bold">

                {item.risk_level}

              </h3>

              <span>

                {item.confidence}%

              </span>

            </div>

            <p className="text-gray-400 mt-3">

              {item.created_at}

            </p>

          </div>

        ))}

      </div>

    </section>

  );

};

export default History;