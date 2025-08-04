// src/app/app.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { Trip } from './models/trip.model';
import { TripService } from './services/trip.service';
import { AddTripModalComponent } from './add-trip-modal/add-trip-modal.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, 
    FormsModule,
    AddTripModalComponent 
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [TripService]
})
export class AppComponent implements OnInit {
  title = 'TripMate Everywhere';
  trips: Trip[] = [];
  isModalVisible = false;

  constructor(private tripService: TripService) {}

  ngOnInit() {
    this.loadTrips();
  }

  loadTrips() {
    this.tripService.getTrips(1).subscribe({
      next: (data) => {
        this.trips = data;
      },
      error: (err) => console.error('Error fetching trips:', err)
    });
  }

  openModal(): void {
    this.isModalVisible = true;
  }

  closeModal(): void {
    this.isModalVisible = false;
  }

  handleSaveTrip(tripData: { name: string; destination: string; start_date: string; end_date: string; budget: number; }): void {
    this.tripService.addTrip(tripData).subscribe({
      next: (response) => {
        console.log('Trip added successfully:', response);
        this.loadTrips();
        this.closeModal();
      },
      error: (err) => console.error('Error adding trip:', err)
    });
  }
}
// The extra '}' at the end of the original file has been removed.
