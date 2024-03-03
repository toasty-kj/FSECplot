import { Component } from '@angular/core'
import { logoBase64 } from '../../../pages/home-page/home-page/logo-image'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent {
  logoImage = logoBase64
  latestRelease = new Date('2024-03-03')
  isWithinOnWeekFromLatestRelease = this.isWithinOneWeek(this.latestRelease)

  /** 今日が最新のリリースから1週間いないかを判別する */
  isWithinOneWeek(release: Date): boolean {
    const today = new Date()
    const oneWeekLater = new Date(
      release.getFullYear(),
      release.getMonth(),
      release.getDate() + 7,
    )
    return today <= oneWeekLater
  }
}
