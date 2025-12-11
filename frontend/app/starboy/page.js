import Link from "next/link";

export default async function systems() {
    const res = await fetch(`http://api:8000/systems`);
    const systems = await res.json();

    if (!systems | systems.error) return <div>No systems found</div>

    return (
        <div className="p-8">
            <h1 className="text-4xl font-bold mb-6 text-rose-700">Systems</h1>

            <ul className="space-y-4">
                {systems.map((system) => (
                    <li key={system.id}>
                        <Link
                            href={`/starboy/${system.id}`}
                            className="block p-4 rounded-xl border-3 border-purple-600 hover:bg-rose-900 transition cursor-pointer"
                        >
                            <h2 className="text-xl font-semibold text-purple-600">
                                {system.name}
                            </h2>
                            <p>Planets: {system.planetCount}</p>
                            <p>{system.galaxy} Galaxy</p>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}