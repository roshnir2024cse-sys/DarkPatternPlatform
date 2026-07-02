import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Stats from "./components/Stats";
import PredictionForm from "./components/PredictionForm";
import History from "./components/History";

function App() {

  return (

    <div className="bg-[#030712] min-h-screen text-white">

      <Navbar />

      <Hero />

      <Stats />

      <PredictionForm />

      <History />

    </div>

  );

}

export default App;