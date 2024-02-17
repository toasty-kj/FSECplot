import { Injectable } from '@angular/core'
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'

@Injectable({
  providedIn: 'root',
})
export class SendDataService {
  URL = 'http://localhost:5001/api'

  constructor(private http: HttpClient) {}

  sendSelectedFilePathList = (pathList: string[]) => {
    return new Promise((resolve, reject) => {
      const params = { pathList: pathList }
      this.http.get(`${this.URL}`, { params: params }).subscribe(
        (response) => {
          resolve(response)
        },
        (error) => {
          reject(error)
        },
      )
    })
  }
}
