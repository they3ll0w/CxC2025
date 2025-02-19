import MainLayout from "@/app/main/layout"

export default function Dashboard() {
    return (
        <MainLayout>
            <div className="h-full flex md:items-center md:justify-center dark:bg-zinc-800 overflow-hidden">
                <h1>Hello, this is the dashboard!</h1>
            </div>
        </MainLayout>
    )
}