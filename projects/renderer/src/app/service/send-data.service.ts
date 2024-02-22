import { Injectable } from '@angular/core'
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'

@Injectable({
  providedIn: 'root',
})
export class SendDataService {
  URL = 'http://localhost:5001/api'

  constructor(private http: HttpClient) {}

  sendSelectedFilePathList = (
    pathList: string[],
    title: string,
    fluorescence: string,
  ) => {
    return new Promise((resolve, reject) => {
      const params = {
        pathList: pathList,
        title: title,
        fluorescence: fluorescence,
      }
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