using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class long_click : MonoBehaviour
{
    public GameObject point1;
    public GameObject point2;

    private float touchTime;
    private bool newTouch;
    public Vector3 initPoint;

    public GameObject obj;

    
    public float left = 2.4f;
    public float right = 4.97f;
    public string name = "0";
    public int flag = 0;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //for (var i = 0; i < 150; i++)
        //{
        //    name = i.ToString();
        //    //Debug.Log(name);
        //    obj = GameObject.Find(name);
        //    Debug.Log("局部坐标:" + obj.transform.localPosition.x);
        //    if (obj.transform.localPosition.x > 2 && obj.transform.localPosition.x < 7)
        //    {
        //        obj.GetComponent<Renderer>().material.SetColor("_EmissionColor", Color.red);
        //    }
        //    //x = obj.transform.localPosition;
        //}


        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hitInfo;
        if (Physics.Raycast(ray, out hitInfo))
        {
            if (Input.touchCount == 1) //一个手指按下的状态            
            {
                Touch touch = Input.GetTouch(0);//有一个手指按下的时候，就记录这个点的属性
                if (touch.phase == TouchPhase.Began)//新按下的
                {
                    newTouch = true;//给一个bool变量
                    touchTime = Time.time;

                }
                else if (touch.phase == TouchPhase.Stationary)//按下没有动
                {
                    if (newTouch == true && Time.time - touchTime > 1f)//经过了第一个if
                    {
                        newTouch = false;//现在是过了一段时间并且是延迟了1f了，就将标志位设为 非新按下
                        flag=get_vector(flag , hitInfo);

                        //Debug.Log("产生碰撞，并且碰撞体的名字是:" + hitInfo.collider.name);
                        //obj = hitInfo.collider.gameObject;
                        //obj.GetComponent<Renderer>().material.SetColor("_EmissionColor", Color.red);
                    }
                }
            }
        }
        
    }

    int get_vector(int flag, RaycastHit hitInfo)//flag=0 or 1
    {

        if (flag < 1)//flag=0
        {
            Destroy(hitInfo.collider.gameObject);
            point1 = hitInfo.collider.gameObject;
            //obj = point1;
            //obj.GetComponent<Renderer>().material.SetColor("_EmissionColor", Color.red);
            
            initPoint = point1.transform.localPosition;
            return 1;
        }
        else//flag=1
        {
            Destroy(hitInfo.collider.gameObject);
            point1 = hitInfo.collider.gameObject;
            initPoint = point1.transform.localPosition;
            return 0;
        }
    }

}
