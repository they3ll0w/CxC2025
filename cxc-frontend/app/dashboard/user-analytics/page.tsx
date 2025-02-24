"use client"

import MainLayout from "@/app/main/layout"
import { Pie, PieChart, Bar, BarChart, CartesianGrid, XAxis } from "recharts"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    ChartConfig,
    ChartContainer,
    ChartLegend,
    ChartLegendContent,
    ChartTooltip,
    ChartTooltipContent,
} from "@/components/ui/chart"
import CustomTooltip from "./custom-tooltip";

const OSPieData = [
    { os: "windows", users: 50, fill: "var(--color-windows)" },
    { os: "linux", users: 30, fill: "var(--color-linux)" },
    { os: "macos", users: 20, fill: "var(--color-macos)" },
    { os: "ios", users: 1, fill: "var(--color-ios)" }
]

const OSChartConfig = {
    users: {
        label: "Users",
    },
    windows: {
        label: "Windows",
        color: "hsl(var(--chart-1))",
    },
    linux: {
        label: "linux",
        color: "hsl(var(--chart-2))",
    },
    macos: {
        label: "macOS",
        color: "hsl(var(--chart-3))",
    },
    ios: {
        label: "iOS",
        color: "hsl(var(--chart-4))",
    },
} satisfies ChartConfig

const eventTimeData = [
    { event: "Account Click", time: 253 },
    { event: "Configurable Table Render", time: 225 },
    { event: "Duplicate Policy Modal - Duplicate Rating", time: 162 },
    { event: "Layout Render", time: 157 },
    { event: "Nav Header - Action Center Click", time: 143 },
    { event: "Nav Header - Help Menu Opened", time: 123 },
    { event: "Nav Header - User Signed Out", time: 120 },
    { event: "Widget Render", time: 119 },
    { event: "All Accounts - Advanced Filters Opened", time: 112 },
    { event: "All Accounts - View", time: 80 },
    { event: "All Accounts - Accounts Table - Account Click", time: 80 },
    { event: "All Accounts - Configurable Table Render", time: 78 },
    { event: "All Accounts - Layout Render", time: 74 },
    { event: "All Accounts - Widget Render", time: 71 }
]

const eventTimeConfig = {
    time: {
        label: "Time (sec)",
        color: "hsl(var(--chart-4))",
    },
} satisfies ChartConfig

export default function UserAnalytics() {
    return (
        <MainLayout>
            <div className="min-h-screen flex flex-col gap-3 md:items-center md:justify-center dark:bg-zinc-800">
                <h1 className="mb-6">User Data - January 2025</h1>
                <div className="w-[90%] grid grid-cols-3 gap-4">
                    <Card className="flex flex-col col-span-2 dark:border-zinc-600 border-zinc-200 dark:bg-zinc-700 bg-zinc-100">
                        <CardHeader className="items-center pb-0">
                            <CardTitle className="text-xs">15 Events with Most Time Spent on Average</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <ChartContainer config={eventTimeConfig}>
                                <BarChart accessibilityLayer data={eventTimeData}>
                                    <CartesianGrid vertical={false} />
                                    {/* <XAxis
                                        dataKey="event"
                                        tickLine={false}
                                        tickMargin={10}
                                        axisLine={false}
                                        tickFormatter={(value) => value.slice(0, 3)}
                                    /> */}
                                    <ChartTooltip
                                        cursor={false}
                                        content={<CustomTooltip />}
                                        labelClassName="text-zinc-700"
                                    />
                                    <Bar dataKey="time" fill="var(--color-time)" radius={8} />
                                </BarChart>
                            </ChartContainer>
                        </CardContent>
                    </Card>

                    <Card className="flex flex-col dark:border-zinc-600 border-zinc-200 dark:bg-zinc-700 bg-zinc-100">
                        <CardHeader className="items-center pb-0">
                            <CardTitle className="text-xs">Pie Chart of Federato Users' OS</CardTitle>
                        </CardHeader>
                        <CardContent className="flex-1 pb-0">
                            <ChartContainer
                                config={OSChartConfig}
                                className="mx-auto aspect-square max-h-[250px]"
                            >
                                <PieChart>
                                    <ChartTooltip
                                        cursor={false}
                                        content={<ChartTooltipContent hideLabel />}
                                    />
                                    <Pie data={OSPieData} dataKey="users" nameKey="os" />
                                    <ChartLegend
                                        content={<ChartLegendContent nameKey="os" />}
                                        className="-translate-y-2 flex-wrap gap-2 [&>*]:basis-1/4 [&>*]:justify-center"
                                    />
                                </PieChart>
                            </ChartContainer>
                        </CardContent>
                    </Card>
                </div>

            </div>
        </MainLayout>
    )
}
