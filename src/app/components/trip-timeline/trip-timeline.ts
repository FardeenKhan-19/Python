// src/app/components/trip-timeline/trip-timeline.ts
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Trip } from '../../models/trip.model';

// Import Angular Material Modules
import { MatCardModule } from '@angular/material/card';
import { MatChipsModule } from '@angular/material/chips';

@Component({
  selector: 'app-trip-timeline',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatChipsModule],
  templateUrl: './trip-timeline.html',
  styleUrls: ['./trip-timeline.css']
})
export class TripTimelineComponent {
  @Input() trip: Trip | null = null;
}