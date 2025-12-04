export default async function dynamicPage({ params }) {
  const { slug } = await params

  return (
    <div> 
      <h1>this what was in the url: {slug}</h1>
    </div>
  )
}