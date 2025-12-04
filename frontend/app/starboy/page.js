import Link from "next/link";

export default async function systems() {
    const res = await fetch(`http://localhost:8000/systems`);
    const systems = await res.json();

    return (
        <div>
            <h1>Systems</h1>
            <ul>
                {systems.map((system) => (
                    <li key={system.id}>
                        <Link href={`/starboy/${system.id}`}>{system.name}</Link>
                        <p>Planets: {system.planetCount}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}