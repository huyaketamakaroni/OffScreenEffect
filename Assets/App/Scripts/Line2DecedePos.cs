﻿using UnityEngine;
using System.Collections;

public class Line2DecedePos : MonoBehaviour {

    private GameObject[] currentObj;
    private int MAX = 6;
    // Use this for initialization
    void Start()
    {
        currentObj = new GameObject[MAX];
        currentObj[0] = GameObject.Find("cgCube2");
        currentObj[1] = GameObject.Find("bothCube1");
        currentObj[2] = GameObject.Find("bareCube5");
        currentObj[3] = GameObject.Find("bareCube1");
        currentObj[4] = GameObject.Find("ledCube1");
        currentObj[5] = GameObject.Find("cgCube1");
    }

    void Update()
    {
        if (this.gameObject == RayCastTest.GetSelectedGameObject())
        {
            //Debug.Log("raycastによってオブジェクトが選択されました。移動する際はキーボード入力を用いてください。");
            /*Yの位置姿勢を変更する*/
            if (Input.GetKeyDown(KeyCode.UpArrow))
            {
                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.y += 0.01f;
                    currentObj[i].transform.position = pos;
                }
                //Debug.Log("UpArrow");
            }
            //下矢印
            else if (Input.GetKeyDown(KeyCode.DownArrow))
            {
                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.y -= 0.01f;
                    currentObj[i].transform.position = pos;
                }

                //Debug.Log("DownArrow");
            }
            //C
            else if (Input.GetKeyDown(KeyCode.C))
            {
                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.x += 0.01f;
                    currentObj[i].transform.position = pos;
                }

                //Debug.Log("C");
            }
            //V
            else if (Input.GetKeyDown(KeyCode.V))
            {

                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.x -= 0.01f;
                    currentObj[i].transform.position = pos;
                }

                //Debug.Log("V");
            }
            //D
            else if (Input.GetKeyDown(KeyCode.D))
            {
                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.z += 0.01f;
                    currentObj[i].transform.position = pos;
                }

                //Debug.Log("D");
            }
            //F
            else if (Input.GetKeyDown(KeyCode.F))
            {

                for (int i = 0; i < MAX; i++)
                {
                    Vector3 pos = currentObj[i].transform.position;
                    pos.z -= 0.01f;
                    currentObj[i].transform.position = pos;
                }

                //Debug.Log("F");
            }



        }
        else
        {
            ;
        }
    }
}
