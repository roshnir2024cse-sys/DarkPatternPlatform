import { motion } from "framer-motion";
import { FaRobot } from "react-icons/fa";

const Hero = () => {
  return (
    <section className="min-h-[90vh] flex items-center justify-center px-8">

      <div className="max-w-7xl w-full grid lg:grid-cols-2 gap-16 items-center">

        {/* LEFT */}

        <motion.div
          initial={{ opacity: 0, x: -80 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
        >

          <h1 className="text-6xl font-black leading-tight">

            Detect

            <span className="bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 bg-clip-text text-transparent">

              {" "}Dark Patterns

            </span>

            <br />

            using AI

          </h1>

          <p className="mt-8 text-xl text-gray-300 leading-9">

            Analyze Amazon products using Machine Learning.

            Detect fake discounts, suspicious pricing,

            and risky shopping patterns instantly.

          </p>

          <div className="mt-10 flex gap-5">

            <button className="px-8 py-4 rounded-xl bg-cyan-500 hover:bg-cyan-400 transition font-bold">

              Analyze Product

            </button>

            <button className="px-8 py-4 rounded-xl border border-cyan-500 hover:bg-cyan-500/20 transition">

              Learn More

            </button>

          </div>

        </motion.div>

        {/* RIGHT */}

        <motion.div
          initial={{ opacity: 0, scale: .8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1 }}
          className="flex justify-center"
        >

          <div className="w-96 h-96 rounded-full bg-cyan-500/20 blur-3xl absolute"></div>

          <FaRobot className="text-[220px] text-cyan-400 relative animate-pulse" />

        </motion.div>

      </div>

    </section>
  );
};

export default Hero;