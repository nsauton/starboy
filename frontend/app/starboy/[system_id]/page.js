import Link from "next/link";

export default async function Planet({ params }) {
    const { system_id } = await params;

    const system_res = await fetch(`http://localhost:8000/systems/${system_id}`);
    const system = await system_res.json();
    
    const planet_res = await fetch(`http://localhost:8000/planets/${system_id}`);
    const planets = await planet_res.json();

    if (!planets | planets.error) return <div>No planets found</div>

    return (
        <div>
            <h1>{system.name}</h1>
            <ul>
                {planets.map((planet) => (
                    <li key={planet.id}>
                        <h1>{planet.name}</h1>
                        <p>type: {planet.type}</p>
                        <p>moons: {planet.moonCount}</p>
                    </li>
                ))}
            </ul>

            <Link href="/starboy">Return to systems</Link>
        </div>
    );
}