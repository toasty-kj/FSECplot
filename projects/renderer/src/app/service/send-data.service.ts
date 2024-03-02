import { Injectable } from '@angular/core'
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'

@Injectable({
  providedIn: 'root',
})
export class SendDataService {
  URL = 'http://localhost:5001/api'

  constructor(private http: HttpClient) {}

  /**ファイルパスからデフォルトのデータ名を取得する */
  getDefaultNameByFilePathList = (
    pathList: string[],
  ): Promise<[{ path: string; name: string }]> => {
    return new Promise((resolve, reject) => {
      const params = {
        pathList: pathList,
      }

      this.http
        .get(`${this.URL}/get-default-data-name`, { params: params })
        .subscribe(
          (response: any) => {
            resolve(response)
          },
          (error) => {
            reject(error)
          },
        )
    })
  }

  sendSelectedFilePathList = (
    pathList: string[],
    dataNameList: string[],
    title: string,
    fluorescence: string,
  ) => {
    return new Promise((resolve, reject) => {
      const params = {
        pathList,
        dataNameList,
        title,
        fluorescence,
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
