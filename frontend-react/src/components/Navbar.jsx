import { FaShieldAlt, FaGithub } from "react-icons/fa";

const Navbar = () => {
  return (
    <nav className="w-full px-10 py-5 flex justify-between items-center backdrop-blur-lg bg-white/10 border-b border-white/20">

      <div className="flex items-center gap-3">

        <FaShieldAlt className="text-4xl text-cyan-400" />

        <h1 className="text-3xl font-bold bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 bg-clip-text text-transparent">
          DarkPattern AI
        </h1>

      </div>

      <ul className="hidden md:flex gap-8 text-white font-medium">

        <li className="hover:text-cyan-400 cursor-pointer transition">
          Home
        </li>

        <li className="hover:text-cyan-400 cursor-pointer transition">
          Dashboard
        </li>

        <li className="hover:text-cyan-400 cursor-pointer transition">
          Analytics
        </li>

        <li className="hover:text-cyan-400 cursor-pointer transition">
          About
        </li>

      </ul>

      <button className="flex items-center gap-2 bg-cyan-500 hover:bg-cyan-400 px-5 py-2 rounded-xl transition">

        <FaGithub />

        GitHub

      </button>

    </nav>
  );
};

export default Navbar;