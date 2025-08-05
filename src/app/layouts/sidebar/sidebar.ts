// src/app/layouts/sidebar/sidebar.ts (FINAL VERSION)

import { Component, OnInit } from '@angular/core'; // Import OnInit
import { CommonModule } from '@angular/common';
import { Trip } from '../../models/trip.model';
import { TripStateService } from '../../services/trip-state'; // <-- Import the service

import { MatListModule } from '@angular/material/list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [CommonModule, MatListModule, MatProgressBarModule, MatIconModule],
  templateUrl: './sidebar.html',
  styleUrls: ['./sidebar.css']
})
export class SidebarComponent implements OnInit {
  activeTripId: number | null = null;
  trips: Trip[] = [];

  // Inject the service into the component's constructor
  constructor(private tripStateService: TripStateService) {}

  ngOnInit(): void {
    // Get the list of trips from the service instead of a hardcoded array
    this.trips = this.tripStateService.getAllTrips();

    // Subscribe to changes in the selected trip to update the highlight
    this.tripStateService.selectedTrip$.subscribe(currentTrip => {
      if (currentTrip) {
        this.activeTripId = currentTrip.id;
      }
    });
  }

  // This method will be called when a user clicks a trip item
  onTripSelect(trip: Trip): void {
    this.tripStateService.setSelectedTrip(trip);
  }

  formatCurrency(value: number): string {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0 }).format(value);
  }
}