import Link from "next/link";

export default function welcomePage() {
    return (
        <>
            <h1>hello world!! Welcome to Starboy, my astronomy/planitarium/star gazing app</h1>
            <Link href={`/starboy`}>Start Galaxy Exploration</Link>
        </>
    )
}