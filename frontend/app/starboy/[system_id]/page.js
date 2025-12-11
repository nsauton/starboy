import Link from "next/link";

export default async function Planet({ params }) {
    const { system_id } = await params;
    
    const res = await fetch(`http://localhost:8000/planets/${system_id}`);
    const planets = await res.json();

    if (!planets | planets.error) return <div>No planets found</div>

    return (
        <div className="p-8">
            <h1 className="text-4xl font-bold mb-6 text-rose-700">{planets.system} System</h1>
            <h1 className="text-4xl font-bold mb-6 text-purple-600">Planets: </h1>

            <ul className="space-y-4">
                {planets.planets.map((planet) => (
                    <li 
                        key={planet.id}
                        className="block p-4 rounded-xl border-3 border-purple-600"
                    >
                        <h2 className="text-xl font-semibold text-purple-600">
                                {planet.name}
                            </h2>
                        <p>type: {planet.type}</p>
                        <p>moons: {planet.moonCount}</p>
                    </li>
                ))}
            </ul>

            <Link 
                href="/starboy"
                className="inline-block text-4xl font-bold text-rose-700 hover:underline mt-6"
            >
                Return to Systems
            </Link>
        </div>
    );
}