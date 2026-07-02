import { motion } from "framer-motion";

const ResultCard = ({ result }) => {

  if (!result) return null;

  const risk = result.RiskLevel.toLowerCase();

  const badgeColor =
    risk === "high"
      ? "bg-red-500"
      : risk === "medium"
      ? "bg-yellow-500"
      : "bg-green-500";

  const recommendation =
    risk === "high"
      ? "Avoid purchasing until verified."
      : risk === "medium"
      ? "Review the product carefully before purchasing."
      : "This product appears relatively safe.";

  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      className="mt-10 rounded-3xl bg-white/5 border border-cyan-500/20 backdrop-blur-xl p-8"
    >

      <div className={`${badgeColor} inline-block px-6 py-2 rounded-full font-bold text-xl`}>
        {result.RiskLevel.toUpperCase()} RISK
      </div>

      <h2 className="text-3xl font-bold mt-6">
        Confidence : {result.Confidence}%
      </h2>

      <div className="w-full bg-gray-700 rounded-full h-4 mt-5">

        <div
          className="bg-cyan-400 h-4 rounded-full transition-all duration-1000"
          style={{ width: `${result.Confidence}%` }}
        />

      </div>

      <div className="mt-8">

        <h3 className="text-2xl font-semibold mb-4">
          🧠 AI Analysis
        </h3>

        <ul className="space-y-2 text-gray-300">

          <li>✔ Machine Learning prediction completed.</li>

          <li>✔ Confidence score calculated.</li>

          <li>✔ Risk category identified.</li>

        </ul>

      </div>

      <div className="mt-8 rounded-xl bg-cyan-500/10 border border-cyan-400 p-5">

        <h3 className="font-bold text-xl">
          Recommendation
        </h3>

        <p className="mt-2 text-gray-300">
          {recommendation}
        </p>

      </div>

    </motion.div>
  );
};

export default ResultCard;