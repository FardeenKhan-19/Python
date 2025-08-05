import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { TripStateService } from '../../services/trip-state';
import { Trip } from '../../models/trip.model';
import { ReactiveFormsModule } from '@angular/forms';

import { StatCardComponent } from '../../components/stat-card/stat-card';
import { TripTimelineComponent } from '../../components/trip-timeline/trip-timeline';
import { FinancialSummaryComponent } from '../../components/financial-summary/financial-summary';
import { CurrencyConverterComponent } from '../../components/currency-converter/currency-converter';

@Component({
  selector: 'app-main-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    CurrencyPipe,
    ReactiveFormsModule,
    StatCardComponent,
    TripTimelineComponent,
    FinancialSummaryComponent,
    CurrencyConverterComponent
  ],
  templateUrl: './main-dashboard.html',
  styleUrls: ['./main-dashboard.css']
})
export class MainDashboardComponent implements OnInit {
  currentTrip: Trip | null = null;

  constructor(private tripStateService: TripStateService) { }

  ngOnInit(): void {
    this.tripStateService.selectedTrip$.subscribe(trip => {
      this.currentTrip = trip;
    });
  }

  getDuration(startDate: string, endDate: string): number {
    const start = new Date(startDate);
    const end = new Date(endDate);
    const diffTime = Math.abs(end.getTime() - start.getTime());
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays + 1;
  }
}