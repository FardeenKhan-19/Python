// src/app/components/stat-card/stat-card.ts (FINAL CORRECTED VERSION)

import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatIconModule
  ],
  templateUrl: './stat-card.html',
  styleUrls: ['./stat-card.css']
})
export class StatCardComponent {
  @Input() title: string = '';
  @Input() value: string | null = ''; // <-- This is the corrected line
  @Input() comment: string = '';
  @Input() icon: string = '';
}