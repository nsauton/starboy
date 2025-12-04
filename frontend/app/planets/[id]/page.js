import Link from "next/link";

export default async function Planet({ params }) {
    const { id } = await params;
    
    const res = await fetch(`http://localhost:8000/planets/${id}`);
    const planet = await res.json();

    if (!planet | planet.error) return <div>Planet not found</div>

    return (
        <div>
            <h1>{planet.name}</h1>
            <p>type: {planet.type}</p>

            <Link href="/planets">Return to planets list</Link>
        </div>
    );
}