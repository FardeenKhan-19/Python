// src/app/services/trip-state.service.ts

import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Trip } from '../models/trip.model';

@Injectable({
  providedIn: 'root'
})
export class TripStateService {
  // A private BehaviorSubject holds the CURRENT value of the selected trip.
  private readonly _selectedTrip = new BehaviorSubject<Trip | null>(null);

  // A public observable that other components can subscribe to for updates.
  readonly selectedTrip$ = this._selectedTrip.asObservable();

  // The master list of trips now lives in the service.
  private allTrips: Trip[] = [
    {
      id: 1,
      name: 'European Adventure',
      destinations: 'Paris, Rome, Barcelona',
      startDate: 'June 15, 2024',
      endDate: 'June 29, 2024',
      budget: 3500,
      spent: 1200,
      status: 'upcoming'
    },
    {
      id: 2,
      name: 'Tokyo Trip',
      destinations: 'Tokyo, Japan',
      startDate: 'April 10, 2024',
      endDate: 'April 15, 2024',
      budget: 2000,
      spent: 2250,
      status: 'completed'
    }
  ];

  constructor() {
    // When the service is first created, automatically select the first trip.
    if (this.allTrips.length > 0) {
      this._selectedTrip.next(this.allTrips[0]);
    }
  }

  // A public method for components to get all trips.
  getAllTrips(): Trip[] {
    return this.allTrips;
  }

  // The public method that components will call to update the selected trip.
  // This "posts the note on the bulletin board".
  setSelectedTrip(trip: Trip): void {
    this._selectedTrip.next(trip);
  }
}