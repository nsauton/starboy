import Link from "next/link";

export default async function Planets() {
    const res = await fetch(`http://localhost:8000/planets`);
    const planets = await res.json();

    return (
        <div>
            <h1>Planets</h1>
            <ul>
                {planets.map((planet) => (
                    <li key={planet.id}>
                        <Link href={`/planets/${planet.id}`}>{planet.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}