import { useState } from "react";
import API from "../services/api";
import ResultCard from "./ResultCard";

const PredictionForm = () => {

  const [formData, setFormData] = useState({
    discount_percentage: "",
    rating: "",
    rating_count: "",
    actual_price: "",
    discounted_price: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {

      const response = await API.post("/predict", {
        discount_percentage: Number(formData.discount_percentage),
        rating: Number(formData.rating),
        rating_count: Number(formData.rating_count),
        actual_price: Number(formData.actual_price),
        discounted_price: Number(formData.discounted_price),
      });

      setResult(response.data);

    } catch (err) {

      console.log(err);

      alert("Prediction Failed");

    }

    setLoading(false);
  };

  return (

    <section className="max-w-6xl mx-auto py-20 px-8">

      <div className="bg-white/5 backdrop-blur-xl rounded-3xl border border-cyan-500/20 p-10">

        <h2 className="text-4xl font-bold mb-10">
          🤖 AI Product Analyzer
        </h2>

        <form
          onSubmit={handleSubmit}
          className="grid md:grid-cols-2 gap-6"
        >

          <input
            type="number"
            placeholder="Discount %"
            name="discount_percentage"
            onChange={handleChange}
            className="p-4 rounded-xl bg-black/20 border border-cyan-500 outline-none"
          />

          <input
            type="number"
            placeholder="Rating"
            name="rating"
            onChange={handleChange}
            className="p-4 rounded-xl bg-black/20 border border-cyan-500 outline-none"
          />

          <input
            type="number"
            placeholder="Review Count"
            name="rating_count"
            onChange={handleChange}
            className="p-4 rounded-xl bg-black/20 border border-cyan-500 outline-none"
          />

          <input
            type="number"
            placeholder="Actual Price"
            name="actual_price"
            onChange={handleChange}
            className="p-4 rounded-xl bg-black/20 border border-cyan-500 outline-none"
          />

          <input
            type="number"
            placeholder="Discounted Price"
            name="discounted_price"
            onChange={handleChange}
            className="p-4 rounded-xl bg-black/20 border border-cyan-500 outline-none"
          />

          <button
            className="bg-cyan-500 hover:bg-cyan-400 rounded-xl p-4 font-bold"
          >
            {loading ? "Analyzing..." : "Analyze Product"}
          </button>

        </form>

        <ResultCard result={result} />

      </div>

    </section>

  );
};

export default PredictionForm;