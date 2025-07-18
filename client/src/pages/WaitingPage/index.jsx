import Header from "@/components/Header";
import { Link } from "react-router";
import { Button } from "@/components/ui/button";
import Footer from "@/components/Footer";

export default function WaitingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-slate-100">
      <Header />
      <div className="flex flex-col items-center justify-center flex-grow gap-5 px-4">
        <h2 className="text-4xl font-bold text-[#538ff8] text-center">
          Submitted Successfully!
        </h2>
        <p className="text-lg text-gray-700 text-center max-w-lg">
          Your details have been saved!
          <br />
          Your SMP details will be informed to you after allocation.
        </p>
        <Link to="/" className="mt-8 max-w-md">
          <Button className="w-full px-4 py-2 bg-[#538ff8] text-white text-sm font-semibold rounded-lg hover:bg-[#4378d6] transition duration-300">
            Go to Home
          </Button>
        </Link>
      </div>
      <Footer></Footer>
    </div>
  );
}
