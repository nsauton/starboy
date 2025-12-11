import Link from "next/link";

export default function welcomePage() {
    return (
        <div className="p-8">
            <h1 className="text-4xl font-bold mb-6 text-rose-700">Welcome to Starboy, my astronomy/planitarium/star gazing app</h1>
            <Link 
                href={`/starboy`}
                className="inline-block p-4 rounded-xl border-3 border-purple-600 hover:bg-rose-900 transition cursor-pointer"
            >
                <h2 className="text-xl font-semibold text-purple-600">
                    Start Galaxy Exploration
                </h2>
            </Link>
        </div>
    )
}