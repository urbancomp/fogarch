//
// Generated file, do not edit! Created by nedtool 5.3 from src/message/BeaconMessage.msg.
//

// Disable warnings about unused variables, empty switch stmts, etc:
#ifdef _MSC_VER
#  pragma warning(disable:4101)
#  pragma warning(disable:4065)
#endif

#if defined(__clang__)
#  pragma clang diagnostic ignored "-Wshadow"
#  pragma clang diagnostic ignored "-Wconversion"
#  pragma clang diagnostic ignored "-Wunused-parameter"
#  pragma clang diagnostic ignored "-Wc++98-compat"
#  pragma clang diagnostic ignored "-Wunreachable-code-break"
#  pragma clang diagnostic ignored "-Wold-style-cast"
#elif defined(__GNUC__)
#  pragma GCC diagnostic ignored "-Wshadow"
#  pragma GCC diagnostic ignored "-Wconversion"
#  pragma GCC diagnostic ignored "-Wunused-parameter"
#  pragma GCC diagnostic ignored "-Wold-style-cast"
#  pragma GCC diagnostic ignored "-Wsuggest-attribute=noreturn"
#  pragma GCC diagnostic ignored "-Wfloat-conversion"
#endif

#include <iostream>
#include <sstream>
#include "BeaconMessage_m.h"

namespace omnetpp {

// Template pack/unpack rules. They are declared *after* a1l type-specific pack functions for multiple reasons.
// They are in the omnetpp namespace, to allow them to be found by argument-dependent lookup via the cCommBuffer argument

// Packing/unpacking an std::vector
template<typename T, typename A>
void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::vector<T,A>& v)
{
    int n = v.size();
    doParsimPacking(buffer, n);
    for (int i = 0; i < n; i++)
        doParsimPacking(buffer, v[i]);
}

template<typename T, typename A>
void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::vector<T,A>& v)
{
    int n;
    doParsimUnpacking(buffer, n);
    v.resize(n);
    for (int i = 0; i < n; i++)
        doParsimUnpacking(buffer, v[i]);
}

// Packing/unpacking an std::list
template<typename T, typename A>
void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::list<T,A>& l)
{
    doParsimPacking(buffer, (int)l.size());
    for (typename std::list<T,A>::const_iterator it = l.begin(); it != l.end(); ++it)
        doParsimPacking(buffer, (T&)*it);
}

template<typename T, typename A>
void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::list<T,A>& l)
{
    int n;
    doParsimUnpacking(buffer, n);
    for (int i=0; i<n; i++) {
        l.push_back(T());
        doParsimUnpacking(buffer, l.back());
    }
}

// Packing/unpacking an std::set
template<typename T, typename Tr, typename A>
void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::set<T,Tr,A>& s)
{
    doParsimPacking(buffer, (int)s.size());
    for (typename std::set<T,Tr,A>::const_iterator it = s.begin(); it != s.end(); ++it)
        doParsimPacking(buffer, *it);
}

template<typename T, typename Tr, typename A>
void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::set<T,Tr,A>& s)
{
    int n;
    doParsimUnpacking(buffer, n);
    for (int i=0; i<n; i++) {
        T x;
        doParsimUnpacking(buffer, x);
        s.insert(x);
    }
}

// Packing/unpacking an std::map
template<typename K, typename V, typename Tr, typename A>
void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::map<K,V,Tr,A>& m)
{
    doParsimPacking(buffer, (int)m.size());
    for (typename std::map<K,V,Tr,A>::const_iterator it = m.begin(); it != m.end(); ++it) {
        doParsimPacking(buffer, it->first);
        doParsimPacking(buffer, it->second);
    }
}

template<typename K, typename V, typename Tr, typename A>
void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::map<K,V,Tr,A>& m)
{
    int n;
    doParsimUnpacking(buffer, n);
    for (int i=0; i<n; i++) {
        K k; V v;
        doParsimUnpacking(buffer, k);
        doParsimUnpacking(buffer, v);
        m[k] = v;
    }
}

// Default pack/unpack function for arrays
template<typename T>
void doParsimArrayPacking(omnetpp::cCommBuffer *b, const T *t, int n)
{
    for (int i = 0; i < n; i++)
        doParsimPacking(b, t[i]);
}

template<typename T>
void doParsimArrayUnpacking(omnetpp::cCommBuffer *b, T *t, int n)
{
    for (int i = 0; i < n; i++)
        doParsimUnpacking(b, t[i]);
}

// Default rule to prevent compiler from choosing base class' doParsimPacking() function
template<typename T>
void doParsimPacking(omnetpp::cCommBuffer *, const T& t)
{
    throw omnetpp::cRuntimeError("Parsim error: No doParsimPacking() function for type %s", omnetpp::opp_typename(typeid(t)));
}

template<typename T>
void doParsimUnpacking(omnetpp::cCommBuffer *, T& t)
{
    throw omnetpp::cRuntimeError("Parsim error: No doParsimUnpacking() function for type %s", omnetpp::opp_typename(typeid(t)));
}

}  // namespace omnetpp

namespace veins_myproject {

// forward
template<typename T, typename A>
std::ostream& operator<<(std::ostream& out, const std::vector<T,A>& vec);

// Template rule which fires if a struct or class doesn't have operator<<
template<typename T>
inline std::ostream& operator<<(std::ostream& out,const T&) {return out;}

// operator<< for std::vector<T>
template<typename T, typename A>
inline std::ostream& operator<<(std::ostream& out, const std::vector<T,A>& vec)
{
    out.put('{');
    for(typename std::vector<T,A>::const_iterator it = vec.begin(); it != vec.end(); ++it)
    {
        if (it != vec.begin()) {
            out.put(','); out.put(' ');
        }
        out << *it;
    }
    out.put('}');
    
    char buf[32];
    sprintf(buf, " (size=%u)", (unsigned int)vec.size());
    out.write(buf, strlen(buf));
    return out;
}

Register_Class(BeaconMessage)

BeaconMessage::BeaconMessage(const char *name, short kind) : ::omnetpp::cPacket(name,kind)
{
    this->posicaoX = 0;
    this->posicaoY = 0;
    this->posRoad = 0;
    this->lenRoad = 0;
    this->speed = 0;
}

BeaconMessage::BeaconMessage(const BeaconMessage& other) : ::omnetpp::cPacket(other)
{
    copy(other);
}

BeaconMessage::~BeaconMessage()
{
}

BeaconMessage& BeaconMessage::operator=(const BeaconMessage& other)
{
    if (this==&other) return *this;
    ::omnetpp::cPacket::operator=(other);
    copy(other);
    return *this;
}

void BeaconMessage::copy(const BeaconMessage& other)
{
    this->idSender = other.idSender;
    this->roadSender = other.roadSender;
    this->TypeDevice = other.TypeDevice;
    this->posicaoX = other.posicaoX;
    this->posicaoY = other.posicaoY;
    this->posRoad = other.posRoad;
    this->lenRoad = other.lenRoad;
    this->speed = other.speed;
}

void BeaconMessage::parsimPack(omnetpp::cCommBuffer *b) const
{
    ::omnetpp::cPacket::parsimPack(b);
    doParsimPacking(b,this->idSender);
    doParsimPacking(b,this->roadSender);
    doParsimPacking(b,this->TypeDevice);
    doParsimPacking(b,this->posicaoX);
    doParsimPacking(b,this->posicaoY);
    doParsimPacking(b,this->posRoad);
    doParsimPacking(b,this->lenRoad);
    doParsimPacking(b,this->speed);
}

void BeaconMessage::parsimUnpack(omnetpp::cCommBuffer *b)
{
    ::omnetpp::cPacket::parsimUnpack(b);
    doParsimUnpacking(b,this->idSender);
    doParsimUnpacking(b,this->roadSender);
    doParsimUnpacking(b,this->TypeDevice);
    doParsimUnpacking(b,this->posicaoX);
    doParsimUnpacking(b,this->posicaoY);
    doParsimUnpacking(b,this->posRoad);
    doParsimUnpacking(b,this->lenRoad);
    doParsimUnpacking(b,this->speed);
}

const char * BeaconMessage::getIdSender() const
{
    return this->idSender.c_str();
}

void BeaconMessage::setIdSender(const char * idSender)
{
    this->idSender = idSender;
}

const char * BeaconMessage::getRoadSender() const
{
    return this->roadSender.c_str();
}

void BeaconMessage::setRoadSender(const char * roadSender)
{
    this->roadSender = roadSender;
}

const char * BeaconMessage::getTypeDevice() const
{
    return this->TypeDevice.c_str();
}

void BeaconMessage::setTypeDevice(const char * TypeDevice)
{
    this->TypeDevice = TypeDevice;
}

double BeaconMessage::getPosicaoX() const
{
    return this->posicaoX;
}

void BeaconMessage::setPosicaoX(double posicaoX)
{
    this->posicaoX = posicaoX;
}

double BeaconMessage::getPosicaoY() const
{
    return this->posicaoY;
}

void BeaconMessage::setPosicaoY(double posicaoY)
{
    this->posicaoY = posicaoY;
}

double BeaconMessage::getPosRoad() const
{
    return this->posRoad;
}

void BeaconMessage::setPosRoad(double posRoad)
{
    this->posRoad = posRoad;
}

double BeaconMessage::getLenRoad() const
{
    return this->lenRoad;
}

void BeaconMessage::setLenRoad(double lenRoad)
{
    this->lenRoad = lenRoad;
}

double BeaconMessage::getSpeed() const
{
    return this->speed;
}

void BeaconMessage::setSpeed(double speed)
{
    this->speed = speed;
}

class BeaconMessageDescriptor : public omnetpp::cClassDescriptor
{
  private:
    mutable const char **propertynames;
  public:
    BeaconMessageDescriptor();
    virtual ~BeaconMessageDescriptor();

    virtual bool doesSupport(omnetpp::cObject *obj) const override;
    virtual const char **getPropertyNames() const override;
    virtual const char *getProperty(const char *propertyname) const override;
    virtual int getFieldCount() const override;
    virtual const char *getFieldName(int field) const override;
    virtual int findField(const char *fieldName) const override;
    virtual unsigned int getFieldTypeFlags(int field) const override;
    virtual const char *getFieldTypeString(int field) const override;
    virtual const char **getFieldPropertyNames(int field) const override;
    virtual const char *getFieldProperty(int field, const char *propertyname) const override;
    virtual int getFieldArraySize(void *object, int field) const override;

    virtual const char *getFieldDynamicTypeString(void *object, int field, int i) const override;
    virtual std::string getFieldValueAsString(void *object, int field, int i) const override;
    virtual bool setFieldValueAsString(void *object, int field, int i, const char *value) const override;

    virtual const char *getFieldStructName(int field) const override;
    virtual void *getFieldStructValuePointer(void *object, int field, int i) const override;
};

Register_ClassDescriptor(BeaconMessageDescriptor)

BeaconMessageDescriptor::BeaconMessageDescriptor() : omnetpp::cClassDescriptor("veins_myproject::BeaconMessage", "omnetpp::cPacket")
{
    propertynames = nullptr;
}

BeaconMessageDescriptor::~BeaconMessageDescriptor()
{
    delete[] propertynames;
}

bool BeaconMessageDescriptor::doesSupport(omnetpp::cObject *obj) const
{
    return dynamic_cast<BeaconMessage *>(obj)!=nullptr;
}

const char **BeaconMessageDescriptor::getPropertyNames() const
{
    if (!propertynames) {
        static const char *names[] = {  nullptr };
        omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
        const char **basenames = basedesc ? basedesc->getPropertyNames() : nullptr;
        propertynames = mergeLists(basenames, names);
    }
    return propertynames;
}

const char *BeaconMessageDescriptor::getProperty(const char *propertyname) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    return basedesc ? basedesc->getProperty(propertyname) : nullptr;
}

int BeaconMessageDescriptor::getFieldCount() const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    return basedesc ? 7+basedesc->getFieldCount() : 7;
}

unsigned int BeaconMessageDescriptor::getFieldTypeFlags(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldTypeFlags(field);
        field -= basedesc->getFieldCount();
    }
    static unsigned int fieldTypeFlags[] = {
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
    };
    return (field>=0 && field<7) ? fieldTypeFlags[field] : 0;
}

const char *BeaconMessageDescriptor::getFieldName(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldName(field);
        field -= basedesc->getFieldCount();
    }
    static const char *fieldNames[] = {
        "idSender",
        "roadSender",
        "TypeDevice",
        "posicaoX",
        "posicaoY",
        "posRoad",
        "lenRoad",
        "speed",
    };
    return (field>=0 && field<7) ? fieldNames[field] : nullptr;
}

int BeaconMessageDescriptor::findField(const char *fieldName) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    int base = basedesc ? basedesc->getFieldCount() : 0;
    if (fieldName[0]=='i' && strcmp(fieldName, "idSender")==0) return base+0;
    if (fieldName[0]=='r' && strcmp(fieldName, "roadSender")==0) return base+1;
    if (fieldName[0]=='T' && strcmp(fieldName, "TypeDevice")==0) return base+2;
    if (fieldName[0]=='p' && strcmp(fieldName, "posicaoX")==0) return base+3;
    if (fieldName[0]=='p' && strcmp(fieldName, "posicaoY")==0) return base+4;
    if (fieldName[0]=='p' && strcmp(fieldName, "posRoad")==0) return base+5;
    if (fieldName[0]=='l' && strcmp(fieldName, "lenRoad")==0) return base+5;
    if (fieldName[0]=='s' && strcmp(fieldName, "speed")==0) return base+6;
    return basedesc ? basedesc->findField(fieldName) : -1;
}

const char *BeaconMessageDescriptor::getFieldTypeString(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldTypeString(field);
        field -= basedesc->getFieldCount();
    }
    static const char *fieldTypeStrings[] = {
        "string",
        "string",
        "string",
        "double",
        "double",
        "double",
        "double",
        "double",
    };
    return (field>=0 && field<7) ? fieldTypeStrings[field] : nullptr;
}

const char **BeaconMessageDescriptor::getFieldPropertyNames(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldPropertyNames(field);
        field -= basedesc->getFieldCount();
    }
    switch (field) {
        default: return nullptr;
    }
}

const char *BeaconMessageDescriptor::getFieldProperty(int field, const char *propertyname) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldProperty(field, propertyname);
        field -= basedesc->getFieldCount();
    }
    switch (field) {
        default: return nullptr;
    }
}

int BeaconMessageDescriptor::getFieldArraySize(void *object, int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldArraySize(object, field);
        field -= basedesc->getFieldCount();
    }
    BeaconMessage *pp = (BeaconMessage *)object; (void)pp;
    switch (field) {
        default: return 0;
    }
}

const char *BeaconMessageDescriptor::getFieldDynamicTypeString(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldDynamicTypeString(object,field,i);
        field -= basedesc->getFieldCount();
    }
    BeaconMessage *pp = (BeaconMessage *)object; (void)pp;
    switch (field) {
        default: return nullptr;
    }
}

std::string BeaconMessageDescriptor::getFieldValueAsString(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldValueAsString(object,field,i);
        field -= basedesc->getFieldCount();
    }
    BeaconMessage *pp = (BeaconMessage *)object; (void)pp;
    switch (field) {
        case 0: return oppstring2string(pp->getIdSender());
        case 1: return oppstring2string(pp->getRoadSender());
        case 2: return oppstring2string(pp->getTypeDevice());
        case 3: return double2string(pp->getPosicaoX());
        case 4: return double2string(pp->getPosicaoY());
        case 5: return double2string(pp->getPosRoad());
        case 6: return double2string(pp->getLenRoad());
        case 7: return double2string(pp->getSpeed());
        default: return "";
    }
}

bool BeaconMessageDescriptor::setFieldValueAsString(void *object, int field, int i, const char *value) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->setFieldValueAsString(object,field,i,value);
        field -= basedesc->getFieldCount();
    }
    BeaconMessage *pp = (BeaconMessage *)object; (void)pp;
    switch (field) {
        case 0: pp->setIdSender((value)); return true;
        case 1: pp->setRoadSender((value)); return true;
        case 2: pp->setTypeDevice((value)); return true;
        case 3: pp->setPosicaoX(string2double(value)); return true;
        case 4: pp->setPosicaoY(string2double(value)); return true;
        case 5: pp->setPosRoad(string2double(value)); return true;
        case 6: pp->setLenRoad(string2double(value)); return true;
        case 7: pp->setSpeed(string2double(value)); return true;
        default: return false;
    }
}

const char *BeaconMessageDescriptor::getFieldStructName(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldStructName(field);
        field -= basedesc->getFieldCount();
    }
    switch (field) {
        default: return nullptr;
    };
}

void *BeaconMessageDescriptor::getFieldStructValuePointer(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc) {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldStructValuePointer(object, field, i);
        field -= basedesc->getFieldCount();
    }
    BeaconMessage *pp = (BeaconMessage *)object; (void)pp;
    switch (field) {
        default: return nullptr;
    }
}

} // namespace veins_myproject

