import { motion } from "framer-motion";
import {
  FaBoxOpen,
  FaBrain,
  FaShieldAlt,
  FaChartLine,
} from "react-icons/fa";

const stats = [
  {
    icon: <FaBoxOpen />,
    number: "12K+",
    title: "Products Analysed",
  },
  {
    icon: <FaBrain />,
    number: "98%",
    title: "AI Accuracy",
  },
  {
    icon: <FaShieldAlt />,
    number: "4",
    title: "Risk Levels",
  },
  {
    icon: <FaChartLine />,
    number: "24/7",
    title: "Prediction Engine",
  },
];

export default function Stats() {
  return (
    <section className="max-w-7xl mx-auto py-20 px-8">

      <div className="grid md:grid-cols-4 gap-8">

        {stats.map((item, index) => (

          <motion.div
            key={index}
            whileHover={{ scale: 1.05 }}
            className="rounded-3xl bg-white/5 border border-cyan-500/20 backdrop-blur-xl p-8 text-center"
          >

            <div className="text-5xl text-cyan-400 flex justify-center mb-5">
              {item.icon}
            </div>

            <h1 className="text-5xl font-bold mb-3">
              {item.number}
            </h1>

            <p className="text-gray-400">
              {item.title}
            </p>

          </motion.div>

        ))}

      </div>

    </section>
  );
}