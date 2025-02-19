"use client";
import React from "react";
import { Spotlight } from "@/components/ui/spotlight-new";
import { HoverBorderGradient } from "@/components/ui/hover-border-gradient";
import Link from "next/link";

export default function Home() {
  return (
    <div className="h-lvh w-full rounded-md flex md:items-center md:justify-center bg-black/[0.96] antialiased bg-dot-white/[0.1] relative overflow-hidden">
      <div className="absolute pointer-events-none inset-0 flex items-center justify-center bg-black [mask-image:radial-gradient(ellipse_at_center,transparent_20%,black)]"></div>
      <Spotlight />
      <div className=" p-4 max-w-7xl  mx-auto relative z-10  w-full pt-20 md:pt-0">
        <h1 className="text-4xl md:text-7xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-b from-neutral-50 to-neutral-400 bg-opacity-50">
          QCxC Analytics
        </h1>
        <p className="mt-4 font-normal text-base text-neutral-300 max-w-lg text-center mx-auto mb-10">
          A submission to the Federato RiskOps Platform Optimization Challenge <br /> CxC 2025
        </p>
        <div className="flex justify-center">
          <Link href="/dashboard">
            <HoverBorderGradient
              containerClassName="rounded-full"
              as="button"
              className="bg-black flex items-center space-x-2"
            >
              <span>Get Started</span>
            </HoverBorderGradient>
          </Link>
        </div>
      </div>
    </div>
  );
}
