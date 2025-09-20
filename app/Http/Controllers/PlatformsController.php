<?php

namespace App\Http\Controllers;

use App\Http\Requests\StorePlatformsRequest;
use App\Http\Requests\UpdatePlatformsRequest;
use App\Models\Platforms;

class PlatformsController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StorePlatformsRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Platforms $platforms)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Platforms $platforms)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdatePlatformsRequest $request, Platforms $platforms)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Platforms $platforms)
    {
        //
    }
}
